# list = [1, 2, 3, 4, 5]
# def calc_total(list):
#     sum = 0
#     for x in list:
#         sum += x
#     print(sum)
# calc_total(list)


#2 separate functions ^^^^^^ calc total vvvvvvvvv even/odd




def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

# --- Put your main program below! ---
def main():
    num = int(input("What is your number?"))
    answer = is_even(num)
    print(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
