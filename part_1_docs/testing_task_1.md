### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # ERROR: Equality check should use double equals "==". Also should be self.card
      return True
    else #ERROR missing ":" after "else"
      return False
   

  dif highest_card(self, card1 card2): # ERROR: Spelling mistake. Should be "def" amd not "dif"! Also, a comma is missing between "card1" and "card2"
  if card1.value > card2.value: #ERROR: card1 and card2 should be prefixed with self.
    return card # ERROR: There is no "card", the function passes in assigned values for "card1" and "card2". Also should be self.card
  else:
    return card2
  


def cards_total(self, cards): #ERROR: This method has been declared outside of the Class due to its (lack of) indentation.
  total #ERROR: The variable "total" has not been declared properly as ot has no assigned start value.
  for card in cards:
    total += card.value # ERROR: should be self.card...
    return "You have a total of" + total
  
```
