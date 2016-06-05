class Director(object):
  '''
  Use builder pattern to construct parking lot.
  '''

  def __init__(self):
    self.builder = None

  def construct_parkinglot(self):
    self.builder.new_parkinglot()
    self.builder.build_floor()
    self.builder.build_size()
    self.builder.location()

  def get_parkinglot(self):
    return self.builder.parkinglot


# abstract builder
class Builder(object):

  def __init__(self):
    self.parkinglot = None

  def new_parkinglot(self):
    self.parkinglot = ParkingLot()

  def build_floor(self):
    raise NotImplementedError

  def build_size(self):
    raise NotImplementedError

  def location(self):
    raise NotImplementedError

  def get_parkinglot(self):
    return self.parkinglot


# concrete builder
class BuilderCityParkingLot(Builder):

  def build_floor(self):
    self.parkinglot.floor = 'more than one'

  def build_size(self):
    self.parkinglot.size = 'big'

  def location(self):
    self.parkinglot.location = 'city'


class BuilderCountryParkingLot(Builder):

  def build_floor(self):
    self.parkinglot.floor = 'one'

  def build_size(self):
    self.parkinglot.size = 'small'

  def location(self):
    self.parkinglot.location = 'country side'


class ParkingLot(object):

  def __init__(self):
    self.floor = None
    self.size = None
    self.location = None

  def __repr__(self):
    return 'floor: {0.floor} | size: {0.size} | location: {0.location}'.format(self)


if __name__ == '__main__':
  director = Director()
  director.builder = BuilderCityParkingLot()
  director.construct_parkinglot()
  city_parkinglot = director.get_parkinglot()
  print(city_parkinglot)

  director.builder = BuilderCountryParkingLot()
  director.construct_parkinglot()
  country_parkinglot = director.get_parkinglot()
  print(country_parkinglot)



