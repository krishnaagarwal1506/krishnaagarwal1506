def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string):
            count = count + 1
        else:
            continue
    return(count)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
# to count how many tines a   sub string comes in a in a string