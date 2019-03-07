class Voter:
  def __init__(self, full_legal_name, dob, ssn, has_voted, salt):
    self.full_legal_name = full_legal_name
    self.dob = dob
    self.ssn = ssn
    self.has_voted = has_voted
    self.salt = salt