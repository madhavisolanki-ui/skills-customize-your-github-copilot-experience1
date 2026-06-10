from utils import greet_student, calculate_rectangle_area, is_palindrome


def main():
    name = input("Enter your name: ")
    print(greet_student(name))

    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))
    area = calculate_rectangle_area(width, height)
    print(f"The area of the rectangle is {area}.")

    word = input("Enter a word to check: ")
    result = is_palindrome(word)
    if result:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")


if __name__ == "__main__":
    main()
