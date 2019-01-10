#!/bin/bash
# 代码提交

Commit(){
  echo "--------函数开始执行----------"
  git pull origin master && echo "拉取成功，查看修改过的文件"
  sleep 3
  git status
  echo "-----准备提交-----"
  echo "请输入注释："
  read a
  git add .
  git commit -m $a
  echo "git 提交注释：$1"
  git push origin master
  echo "-----提交结束-----"
  echo "--------函数执行结束----------"
}

Commit
