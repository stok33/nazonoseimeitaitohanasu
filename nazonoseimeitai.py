#!/usr/bin/env python
# 謎の生命体と会話するプログラム
import random
import hashlib

def hashinput():
    return hashlib.sha256(input().encode()).hexdigest()

print("( .ω.)よよよ！")

print("(.ω.)よよよ〜")
if hashinput() == "7a0a3e30c7c42e14524f50d3681c4cbd6faf5d9e97cb31b8f2e02476bfdfb2b1":
	print("ここで交信が途切れた")
else:
	print("(.ω.)よ！？よよよ♪")
	if hashinput() == "4864c406c9ccab1e5d22e3280d0fd023f74f7be0034f3d3fe53b1167ee7668ee":
		print("(.ω.)よよよよっ！よよっよよよよよよよ！")

	else:
		print("(.ω.)よよよよ？")
		if hashinput() == "c09f863923bfc462b41d02fad3010a3cbb7fa5e3847dad3ea27cd6f1d50cf638":
			print("(.ω.)！よよよよ！よよ。よ〜")
		else:
			if random.random() < 0.1:
				print("(.ω.)きみのほしはいいところだね　いってみようかな　まっててね")
			else:
				print("(.ω.)よよ///……よよ♡")


