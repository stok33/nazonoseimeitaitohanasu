#!/usr/bin/env python
# 謎の生命体と会話するプログラム
import random

print("( .ω.)よよよ！")

print("(.ω.)よよよ〜")
if input() ==  "よ":
	print("ここで交信が途切れた")
else:
	print("(.ω.)よ！？よよよ♪")
	if input() ==  "よよよ":
		print("(.ω.)よよよよっ！よよっよよよよよよよ！")

	else:
		print("(.ω.)よよよよ？")
		if input() == "よよよよ":
			print("(.ω.)！よよよよ！よよ。よ〜")
		else:
			if random.random() < 0.1:
				print("(.ω.)きみのほしはいいところだね　いってみようかな　まっててね")
			else:
				print("(.ω.)よよ///……よよ♡")
