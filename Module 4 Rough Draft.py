Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Attributes
>>> item_name = 'string'
>>> item_price = float(0.0)
>>> item_quantity = int(0)
>>> # Default constructor
>>> define Items:
  File "<stdin>", line 1
    define Items:
           ^^^^^
SyntaxError: invalid syntax
>>> define_Items:
  File "<stdin>", line 1
    define_Items:
                 ^
SyntaxError: invalid syntax
>>> def items:
  File "<stdin>", line 1
    def items:
             ^
SyntaxError: expected '('
>>> def items: (item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
  File "<stdin>", line 1
    def items: (item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
             ^
SyntaxError: expected '('
>>>  def items(item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
  File "<stdin>", line 1
    def items(item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
IndentationError: unexpected indent
>>> def items: (item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
  File "<stdin>", line 1
    def items: (item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
             ^
SyntaxError: expected '('
>>> def items(item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
  File "<stdin>", line 1
    def items(item_name = "none", item_price = float(f'{0.0:.2f}'), item.quantity = int(0))
                                                                        ^
SyntaxError: invalid syntax
>>> class Item:
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after class definition on line1
>>> def Items:
  File "<stdin>", line 1
    def Items:
             ^
SyntaxError: expected '('
>>> class Items:
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after class definition on line1
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> class Items:
... item_Name = "none"
  File "<stdin>", line 2
    item_Name = "none"
    ^
IndentationError: expected an indented block after class definition on line1
>>> class Items:
... item_name = "none"
  File "<stdin>", line 2
    item_name = "none"
    ^
IndentationError: expected an indented block after class definition on line1
>>> class Items:
... def Items:
  File "<stdin>", line 2
    def Items:
    ^
IndentationError: expected an indented block after class definition on line1
>>> class Items:
... def __init__(self):
  File "<stdin>", line 2
    def __init__(self):
    ^
IndentationError: expected an indented block after class definition on line1
>>> class Items:
...     def__init__(self):
  File "<stdin>", line 2
    def__init__(self):
                     ^
SyntaxError: invalid syntax
>>> def__init__(self):
  File "<stdin>", line 1
    def__init__(self):
                     ^
SyntaxError: invalid syntax
>>> class Items:
...     def__init__(self): self.item_name = "none", self.item_price = 0.0, s
elf.item_quantity = 0
  File "<stdin>", line 2
    def__init__(self): self.item_name = "none", self.item_price = 0.0, self.item_quantity = 0
    ^^^^^^^^^^^^^^^^^
SyntaxError: illegal target for annotation
>>> class Item:
...     def __init__(self):
...             self.item_name = "none"
...             self.item_price = 0.0
...             self.item_quantity = 0
...
>>>
>>> # Method
>>>
>>>
>>>
>>>
>>>
>>>
>>> item_name = 'Bottled Water'
>>> item_price = 1.00
>>> item_quantity = 10
>>>
>>> # Method
>>> def print_item_cost(item_name, item_quantity, @, $item_price, =, $item_quantity)
  File "<stdin>", line 1
    def print_item_cost(item_name, item_quantity, @, $item_price, =, $item_quantity)
                                                  ^
SyntaxError: invalid syntax
>>> def print_item_cost(item_name, item_quantity, '@', $item_price, '=', $it
em_quantity)
  File "<stdin>", line 1
    def print_item_cost(item_name, item_quantity, '@', $item_price, '=', $item_quantity)
                                                  ^^^
SyntaxError: invalid syntax
>>> print(item_name, item_quantity, '@', $item_price, '=', $item_quantity)
  File "<stdin>", line 1
    print(item_name, item_quantity, '@', $item_price, '=', $item_quantity)
                                         ^
SyntaxError: invalid syntax
>>> print(item_name, item_quantity, '@', $ item_price, '=', $ item_quantity)

  File "<stdin>", line 1
    print(item_name, item_quantity, '@', $ item_price, '=', $ item_quantity)
                                         ^
SyntaxError: invalid syntax
>>> print(item_name, item_quantity, '@', '$',item_price, '=', '$',item_quant
ity)
Bottled Water 10 @ $ 1.0 = $ 10
>>> print(item_name, item_quantity, '@', '$',int(item_price), '=', '$',item_
quantity)
Bottled Water 10 @ $ 1 = $ 10
>>>
>>> def print_item_cost(self):
...     print(f'{(self.item_name) (self.item_quantity) @ $(self.item_price)
= $(self.item_price * self.item_quantity)})"
  File "<stdin>", line 2
    print(f'{(self.item_name) (self.item_quantity) @ $(self.item_price) = $(self.item_price * self.item_quantity)})"
                                                   ^
SyntaxError: f-string: expecting '=', or '!', or ':', or '}'
>>>     print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} =
 ${self.item_price * self.item_quantity})"
  File "<stdin>", line 1
    print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity})"
IndentationError: unexpected indent
>>>     print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')
  File "<stdin>", line 1
    print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')
IndentationError: unexpected indent
>>> def print_item_cost:
  File "<stdin>", line 1
    def print_item_cost:
                       ^
SyntaxError: expected '('
>>> def print_item_cost(self):
...     print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')
...
>>>
>>> # Step 2
>>> item1 = "Chocolate Chips"
>>> item1_price = 3
>>> item1_quantity = 1
>>> item2 = "Bottled Water"
>>> item2_price = 1
>>> item2_quantity = 10
>>>
>>> item1_cost = item1_price * item1_quantity
>>> print(item1_cost)
3
>>> item2_cost = item2_price * item2_quantity
>>> print(item2_cost)
10
>>>
>>> # Step 3
>>> print('TOTAL COST' /n
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cos
t) /n
  File "<stdin>", line 1
    print('TOTAL COST' /n
          ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('TOTAL COST' /n,
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n,
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cos
t) /n,
... 'Total:', '${}.format(item1_cost+item2_cost)')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> print('TOTAL COST' /n,
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost) /n,
  File "<stdin>", line 2
    '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('TOTAL COST' /n,
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n,
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost) /n,
... 'Total:', '${}.format(item1_cost+item2_cost)' n/)
  File "<stdin>", line 4
    'Total:', '${}.format(item1_cost+item2_cost)' n/)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('TOTAL COST' /n,
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n,
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost) /n,
... 'Total:', '${}.format(item1_cost+item2_cost)' n/,
  File "<stdin>", line 4
    'Total:', '${}.format(item1_cost+item2_cost)' n/,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('TOTAL COST' /n,
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n,
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost) /n,
... 'Total:', '$(item1_cost+item2_cost)' n/,
  File "<stdin>", line 4
    'Total:', '$(item1_cost+item2_cost)' n/,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('TOTAL COST' /n,
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n,
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost) /n,
... 'Total:', '$', (item1_cost+item2_cost)')
  File "<stdin>", line 4
    'Total:', '$', (item1_cost+item2_cost)')
                                          ^
SyntaxError: unterminated string literal (detected at line 4)
>>> print('TOTAL COST' /n,
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost) /n,
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost) /n,
... 'Total:', '$', (item1_cost+item2_cost))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> print('TOTAL COST/n',
... ''{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_co
st)/n',
  File "<stdin>", line 2
    ''{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost)/n',
    ^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('TOTAL COST/n',
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cos
t)/n,
... '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost)/n,
... 'Total:', '$', (item1_cost+item2_cost))
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'n' is not defined
>>> print("TOTAL COST/n'{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cos
  File "<stdin>", line 1
    print("TOTAL COST/n'{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cos
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> t)/n
  File "<stdin>", line 1
    t)/n
     ^
SyntaxError: unmatched ')'
>>>
>>>
>>> print("TOTAL COST/n'{} {} @ ${} = ${}'.format(item1, item1_quantity,item
1_price,item1_cost)/n'{} {} @ ${} = ${}'.format(item2, item2_quantity, item2
_price, item2_cost)/nTotal: $(item1_cost+item2_cost)")
TOTAL COST/n'{} {} @ ${} = ${}'.format(item1, item1_quantity,item1_price,item1_cost)/n'{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost)/nTotal: $(item1_cost+item2_cost)
>>> print('TOTAL COST/n',
... '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost)/n,
...
...
...
...
...
...
... )
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'n' is not defined
>>>
>>> print('TOTAL COST')
TOTAL COST
>>> print('{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost))
Chocolate Chips 1 @ $3 = $3
>>> print('{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_price, item2_cost))
Bottled Water 10 @ $1 = $10
>>> print('Total: $', (item1_cost + item2_cost))
Total: $ 13
>>>  print('TOTAL COST/n', "'{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost)/n")
  File "<stdin>", line 1
    print('TOTAL COST/n', "'{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost)/n")
IndentationError: unexpected indent
>>> print('TOTAL COST/n', "'{} {} @ ${} = ${}'.format(item1, item1_quantity,
 item1_price, item1_cost)/n")
TOTAL COST/n '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price,item1_cost)/n
>>> print('TOTAL COST'/n, "'{} {} @ ${} = ${}'.format(item1, item1_quantity,
 item1_price, item1_cost)/n")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> print('TOTAL COST'\n, "'{} {} @ ${} = ${}'.format(item1, item1_quantity,
 item1_price, item1_cost)"\n)
  File "<stdin>", line 1
    print('TOTAL COST'\n, "'{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost)"\n)
                       ^
SyntaxError: unexpected character after line continuation character
>>> print('TOTAL COST\n', "'{} {} @ ${} = ${}'.format(item1, item1_quantity,
 item1_price, item1_cost)\n")
TOTAL COST
 '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost)

>>> print('TOTAL COST\n', "{} {} @ ${} = ${}.format(item1, item1_quantity, i
tem1_price, item1_cost)\n")
TOTAL COST
 {} {} @ ${} = ${}.format(item1, item1_quantity, item1_price, item1_cost)

>>> print('TOTAL COST\n', '{} {} @ ${} = ${}'.format(item1, item1_quantity,
item1_price, item1_cost)\n)
  File "<stdin>", line 1
    print('TOTAL COST\n', '{} {} @ ${} = ${}'.format(item1, item1_quantity,item1_price, item1_cost)\n)

                         ^
SyntaxError: unexpected character after line continuation character
>>>
>>> item1_line = '{} {} @ ${} = ${}'.format(item1, item1_quantity, item1_price, item1_cost)
>>> item2_line = '{} {} @ ${} = ${}'.format(item2, item2_quantity, item2_pri
ce, item2_cost)
>>> print("TOTAL COST\n", 'item1_line\n', 'item2_line\n', 'Total: $'(item1_c
ost+item2_cost))
<stdin>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> print("TOTAL COST\n", 'item1_line,\n', 'item2_line,\n', 'Total: $'(item1
_cost+item2_cost))
<stdin>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> print("TOTAL COST\n", item1_line, '\n', item2_line, '\n', 'Total: $'(ite
m1_cost+item2_cost))
<stdin>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> print("TOTAL COST\n", item1_line, item2_line, 'Total: $'(item1_cost+item
2_cost))
<stdin>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> print(iten1_line)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'iten1_line' is not defined. Did you mean: 'item1_line'?
>>> print(item1_line)
Chocolate Chips 1 @ $3 = $3
>>> print(item1_line, item2_line)
Chocolate Chips 1 @ $3 = $3 Bottled Water 10 @ $1 = $10
>>> print('item1_line\n', item2_line)
item1_line
 Bottled Water 10 @ $1 = $10
>>> print(item1_line'\n', item2_line)
  File "<stdin>", line 1
    print(item1_line'\n', item2_line)
                    ^^^^
SyntaxError: invalid syntax
>>> print(item1_line, '\n', item2_line)
Chocolate Chips 1 @ $3 = $3
 Bottled Water 10 @ $1 = $10
>>> print(item1_line, '\n',item2_line, '\n', 'Total: $', (item1_cost + item2_cost))
Chocolate Chips 1 @ $3 = $3
 Bottled Water 10 @ $1 = $10
 Total: $ 13
>>> print('\nTOTAL COST\n', item1_line, '\n',item2_line, '\n', 'Total: $', (
item1_cost + item2_cost))

TOTAL COST
 Chocolate Chips 1 @ $3 = $3
 Bottled Water 10 @ $1 = $10
 Total: $ 13
>>> print('TOTAL COST\n', item1_line, '\n',item2_line, '\n', 'Total: $', (it
em1_cost + item2_cost))
TOTAL COST
 Chocolate Chips 1 @ $3 = $3
 Bottled Water 10 @ $1 = $10
 Total: $ 13
>>> print(' TOTAL COST\n', item1_line, '\n',item2_line, '\n', 'Total: $', (i
tem1_cost + item2_cost))
 TOTAL COST
 Chocolate Chips 1 @ $3 = $3
 Bottled Water 10 @ $1 = $10
 Total: $ 13
>>>
