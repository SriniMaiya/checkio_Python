#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run yaml-simple-dict
def yaml(a):
    # your code here
    a = a.split("\n")
    a = [x.split(":") for x in a if len(x) >0]

    return  {x[0].strip(" "): int(x[1]) if x[1].strip(" ").isdigit() else x[1].strip(" ") for x in a}



if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))
    print( yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")

x 
