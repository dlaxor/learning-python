### 외부 라이브러리

## ar

from faker import Faker
a = Faker('ko-KR')

print(a.name())
print(a.address())
print(a.text())