class Vector:

  def __init__(self, d):
    if isinstance(d, float):
      raise ValueError('Float is not supported')
    if isinstance(d, int):
      self._coords = [0] * d
    else:
      self._coords = list(d)
  
  def __len__(self):
    return len(self._coords)
  
  def __getitem__(self, j):
    return self._coords[j]
    
  def __setitem__(self, j, val):
    self._coords[j] = val
    
  def __add__(self, other):
    if len(self) != len(other):
      raise ValueError('dimension must agree')
    
    result = Vector(len(self))
    
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    
    return result
  
  def __eq__(self, other):
    return self._coords == other._coords
    
  def __str__(self):
    return "<" + str(self._coords)[1:-1] + ">" # [1:-1] and str(self._coords)[1:-1], how?
  
  def __sub__(self, other):
    if len(self) != len(other):
      raise ValueError('dimension must agree')
      
    result = Vector(len(self))
    
    for j in range (len(self)):
      result[j] = self[j] - other[j]
    
    return result

  def __neg__(self):
    
    result = Vector(len(self))
    
    for i in range(len(self)):
      result[i] = -1 * self[i]
      
    return result
    
  def __radd__(self, other):
    if len(self) != len(other):
      raise ValueError('dimension must agree')
    
    result = Vector(len(self))
    
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    
    return result

  def __mul__(self,other):
  
    if isinstance(other, (int, float)):
      result = Vector(len(self))
    
      for i in range(len(self)):
        result[i] = self[i] * other
      
      return result
    
    elif isinstance(other, Vector):
        if len(self) == len(other):
          
          total = 0
          for i in range(len(self)):
            total += self[i] * other[i]
    
          return total
        else:
          raise ValueError('dimension must agree')
    
    else:
      raise ValueError('unsupported type')
      
  def __rmul__(self, other):
    return self.__mul__(other)
    