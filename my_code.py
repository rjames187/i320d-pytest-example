import pytest

def fix_phone_num(phone_num_to_fix):
  # given "5125558823". Split the parts, then recombine and return
  if '-' in phone_num_to_fix:
    area_code = phone_num_to_fix[0:3]
    three_part = phone_num_to_fix[4:7]
    four_part = phone_num_to_fix[8:12]
  elif '(' in phone_num_to_fix:
    area_code = phone_num_to_fix[1:4]
    three_part = phone_num_to_fix[6:9]
    four_part = phone_num_to_fix[10:14]
  else: 
    area_code = phone_num_to_fix[0:3] # 512 (first three digits)
    three_part = phone_num_to_fix[3:6] # 555 (next three digits)
    four_part = phone_num_to_fix[6:10] # # 8823 (last four digits)

  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_other_formats():
  assert fix_phone_num("555-442-98761") == '(555) 442 9876'
  assert fix_phone_num("(321) 654 3333") == '(321) 654 3333'

def test_another_fail():
  assert 1 == 1
  assert 3 == 3
