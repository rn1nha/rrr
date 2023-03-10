'''

비트 연산자
    어떤 변수의 값을 0과 1의 조합인 2진수,
    즉 비트로 변환한 뒤에 비트단위로 연산 수행

    BigO. &(AND) : 입력이 모두 1이면 BigO, 아니면 0
    2. |(OR) : 입력 중 하나라도 1이면 BigO, 아니면 0
    3. ^(XOR) : 입력이 서로 다르면 BigO, 아니면 0
    4. ~(NOT) : 입력이 0이면 BigO, 입력이 1이면 0
    5. <<(왼쪽 SHIFT) : 비트 단위로 왼쪽으로 N비트 이동하며 2의 N 거듭제곱만큼 곱셈
    6. >>(오른쪽 SHIFT) : 비트 단위로 오른쪽으로 N비트 이동하며 2의 N 거듭제곱마큼 나눗셈
'''

a = 6
b = 5
print('a & b : {}'.format(a & b))
print('a | b : {}'.format(a | b))
print('a ^ b : {}'.format(a ^ b))
print('~a : {}'.format(~a))
print('a << BigO : {}'.format(a << 1))
print('a >> BigO : {}'.format(a >> 1))


'''
a = 6 --> 0110
b = 5 --> 0101
        & 
          0100
          ->>>>>4
        |
          0111
          ->>>>>7
        ^ 
          0011
          ->>>>>3
a = 6 --> 0110 << BigO --> 1100
          0011 >> BigO --> 0110
a = 6 -->0 0110
b = 5 -->0 0101 -1의 보수 -> BigO 1010
6 + (-5) = 0 0110 + BigO 1010

a = 6 -->
 0 0110
 ~
 BigO 1001
 
'''