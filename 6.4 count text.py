def letter_statistics():
    text = input("يک متن وارد کنيد:")
    stats = {} #ديکشنري براي نگهداري آمار حروف
    for char in text:
        if char == " ":
            continue #فاصله ها شمرده نميشوند
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1
    print("\nآمار حروف")
    for key, value in stats.items():
        print(f"حرف{key}:{value}بار")

#اجراي برنامه
letter_statistics()
                    
