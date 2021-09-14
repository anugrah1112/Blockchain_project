import time 
import hashlib
class Add_Block:

  def __init__(self, string, previous_hash = None):
    self.string = str(string)
    self.previous_hash = str(previous_hash)
    self.time_stamp = str(time.time())
    self.hash = str(self.calculate_hash())
    self.block_data = self.string + self.previous_hash + self.time_stamp + self.hash
    print("Contents of the block are : " + self.block_data)

  def calculate_hash(self):
    string_value = self.previous_hash + self.time_stamp + self.string
    result = hashlib.md5(string_value.encode())
    print(result.hexdigest())
    return result.hexdigest()


def checkLuhn(cardNo):
     
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False

def main():
  card_number = list(input("Please enter a card number : ").strip())
  check = checkLuhn(card_number)

  if check is False:
    print("Re-enter correct details")
      
  elif check is True:
    print("The entered details are correct.")
    print(card_number)
    str1 = str(card_number[0:4])
 
    str2 = str(card_number[4:8])

    str3 = str(card_number[8:12])

    str4 = str(card_number[12:16])
    
    
    block_1 = Add_Block(str1)
    block_2 = Add_Block(str2, block_1.hash)
    block_3 = Add_Block(str3, block_2.hash)
    block_4 = Add_Block(str4, block_3.hash)

    



if __name__ == "__main__":
    main()
