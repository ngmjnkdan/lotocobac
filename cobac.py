while True:
	i = int(input("📍Số may mắn nằm trong từ 1 đến 1000:  "))
	if i < 90:
		print('Số bạn đoán hơi nhỏ,chọn số khác đi 🙏')
	elif i < 100:
		print('Đoán gần đúng rồi cố lên 🧠')
	elif i == 100:
		print("Chúc mừng bạn đã đoán trúng ✅")
		break
	else:
		print('Bạn đoán chưa đúng rồi ❌')
