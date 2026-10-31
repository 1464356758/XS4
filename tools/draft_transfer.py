#!/usr/bin/env python3
"""合并来自GitHub草稿目录的UTF-8片段；只生成当前未采用章的草稿，不采用或更改正式事实。"""
import argparse
import hashlib
from pathlib import Path
import re
import sys
import json
import novel_state as ns


def main():
    p=argparse.ArgumentParser()
    p.add_argument('command',choices=['assemble'])
    p.add_argument('--out',required=True)
    p.add_argument('--sha256',required=True)
    p.add_argument('--parts',nargs='+',required=True)
    a=p.parse_args()
    root=Path('.').resolve()
    state=ns.load_state(root/'book')
    ns.verify_files(root/'book',state)
    chapter=len(state['chapters'])+1
    expected_out=f'drafts/CH{chapter:03d}.txt'
    ns.require(a.out==expected_out,'只能合并当前未采用章的固定草稿目标')
    ns.require(re.fullmatch('[0-9a-f]{64}',a.sha256) is not None,'需要完整预期SHA256')
    ns.require(2<=len(a.parts)<=20,'要求2至20个有序片段')
    fragments=[]
    for i,raw in enumerate(a.parts,1):
        ns.require(raw==f'drafts/CH{chapter:03d}_part_{i:02d}.txt','片段必须连续编号且位于当前章草稿目录')
        path=ns.inside(root,raw)
        ns.require(path.is_file() and not path.is_symlink(),'片段不存在或是符号链接')
        data=path.read_text(encoding='utf-8')
        ns.require(bool(data) and len(data)<=20000,'片段为空或过大')
        fragments.append(data)
    body=''.join(fragments)
    ns.require(hashlib.sha256(body.encode('utf-8')).hexdigest()==a.sha256,'完整正文与预期SHA256不一致')
    count=ns.han_count(body)
    ns.require(state['config']['chapter_han_min']<=count<=state['config']['chapter_han_max'],'正文汉字数不足或超限')
    out=ns.inside(root,a.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    ns.immutable_text(out,body)
    print(json.dumps({'path':a.out,'sha256':a.sha256,'han_count':count,'parts':len(fragments),'chapter':chapter},ensure_ascii=False))


if __name__=='__main__':
    try:main()
    except (ns.WorkspaceError,OSError,UnicodeError) as e:sys.exit('未完成：'+str(e))
