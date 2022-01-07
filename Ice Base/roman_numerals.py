#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run roman-numerals

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }Roman numerals come from the ancient Roman numbering system.  They are based on specific letters of the alphabet which are combined to signify the sum  (or, in some cases, the difference) of their values. The first ten Roman  numerals are:
# 
# I, II, III, IV, V, VI, VII, VIII, IX, and X.
# 
# The Roman numeral system is decimal based, but not directly positional and does not  include a zero. Roman numerals are based on combinations of these seven symbols:
# 
# NumeralValueI1 (unus)V5 (quinque)X10 (decem)L50 (quinquaginta)C100 (centum)D500 (quingenti)M1,000 (mille)More additional information about Roman numerals can be found onthe Wikipedia article.
# 
# For this task, you should return a Roman numeral using the specified integer value ranging from 1 to 3999.
# 
# Input:A number as an integer.
# 
# Output:The Roman numeral as a string.
# 
# Precondition:0 < number < 4000
# 
# 
# END_DESC

def checkio(data):

    #replace this for solution
    return ""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')