import re
# 정규표현식(이하 정규식)은 특정 문자열의 패턴을 표현하는 식.
# 복잡한 표현을 보다 간결하게 표현할 수 있음.
# re 모듈을 통해 사용 가능하며, 일치시키려는 가능한 문자열 집합에 대한 규칙을 정의함.

# 메타 문자(Meta Character)는 문자열 양식을 나타내는 일종의 특수기호.
# . ^ $ * + ? { } [ ] \ | () 로 표현.

# . 임의의 모든 문자가 1개 나오는가?
dot = re.compile('a.b')
print(dot.match('acb'))
print(dot.match('ab'))

# ^ 줄의 시작을 표현.
upd = re.compile('^a')
print(upd.match('abc'))
print(upd.match('bcd'))

# $ 줄의 끝을 표현.
endd = re.compile('you$')
print(endd.search('thank you'))
print(endd.search('thanks'))

# | 또는(or)의 의미를 표현.
dor = re.compile('a|b')
print(dor.match('and'))
print(dor.match('birds'))

# [ ] 대괄호 안에서 문자(열).
dai = re.compile('[you]')
print(dai.search('thank you'))
print(dai.search('never mind'))

# [ ^ ] 해당 문자(열) 제외.
exc = re.compile('[^you]')
print(exc.search('your life'))
print(exc.findall('kyoudai'))

# [ - ] 범위 지정.
rd = re.compile('[3-5]')
print(rd.search('121687'))
print(rd.findall('123456'))

# ( ) 그룹 지정.
gp = re.compile('(you)')
print(gp.search('ryoukai'))
print(gp.findall('youtube'))

# 숫자와 문자와 관련한 것
# \d = [0-9]와 동일 의미.
# \D = [^0-9]와 동일 의미.
# \s = 공백 문자(white space)를 의미.
# \S = 공백 문자를 제외한 모든 것.
# \b = 단어의 시작과 끝의 빈 공백.
# \B = 단어의 시작과 끝의 빈 공백을 제외한 빈 공백.
# \w = 숫자와 알파벳 문자를 의미. [a-zA-Z0-0].
# \W = 숫자와 알파벳 문자를 제외한 모든 것.

# 반복을 나타내는 메타 문자.
# ( * ) = 0회 이상 반복.
rp = re.compile('do*g')
print(rp.search('dg'))
print(rp.search('dog'))

# ( + ) = 1회 이상 반복.
rrp = re.compile('du+ck')
print(rrp.search('dck'))
print(rrp.search('duck'))

# ( { } ) = 반복 회수 지정.
drp = re.compile('ro{2}k')
print(drp.search('rok'))
print(drp.search('rook'))
rdrp = re.compile('lo{2,4}k')
print(rdrp.search('lok'))
print(rdrp.search('look'))

# 식1(?=식2) = 식1 뒤의 문자열이 식2와 매치되면 식1 매치.
# 식1(?!식2) = 식1 뒤의 문자열이 식2와 매치되지 않으면 식1 매치.
# (?<=식1)식2 = 식2 앞의 문자열이 식1와 매치되면 식2 매치.
# (?<!식1)식2 = 식2 앞의 문자열이 식1와 매치되지 않으면 식2 매치.

# 정규식을 이용한 문자열 검색
# match() = 문자열의 처음부터 정규식과 매치되는지 조사.
# search() = 문자열 전체를 검색하여 정규식과 매치되는지 조사.
# findall() = 정규식과 매치되는 모든 문자열을 리스트로 반환.
# finditer() = 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 반환.

# 참고
# https://docs.python.org/ko/3/howto/regex.html
# https://wikidocs.net/21703
# https://spidyweb.tistory.com/373