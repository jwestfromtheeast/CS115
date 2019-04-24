'''
Created on 23 April 2019
@author:   Justin Westley
@username: jwestley
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        """
        Returns a new object with the same month, day, year
        as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        """
        Decides if self and d2 represent the same calendar date,
        whether or not they are in the same place in memory
        """
        return self.year == d2.year and self.month == d2.month \
            and self.day == d2.day
    
    def tomorrow(self):
        """
        Changes the calling object to represent the next calendar day
        """
        if self.day == DAYS_IN_MONTH[self.month]:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1
    
    def yesterday(self):
        """
        Changes the calling object to represent the previous calendar day
        """
        if self.day == 1:
            if self.month == 1:
                self.month = 12
                self.year -= 1
                self.day = 31
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1

    def addNDays(self, N):
        """
        Changes the calling object to represent N calendar days in the future
        """
        print(self)
        for n in range(N):
            self.tomorrow()
            print(self)
            
    def subNDays(self, N):
        """
        Changes the calling object to represent N calendar days in the past
        """
        print(self)
        for n in range(N):
            self.yesterday()
            print(self)
    
    def isBefore(self, d2):
        """
        Returns True if the calling date is before d2, and False otherwise
        """
        if self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        else:
            if self.month < d2.month:
                return True
            elif self.month > d2.month:
                return False
            else:
                if self.day < d2.day:
                    return True
                elif self.day > d2.day:
                    return False
                else:
                    return False
    
    def isAfter(self, d2):
        """
        Returns True is the calling date is after d2, and False otherwise
        """
        if self.year > d2.year:
            return True
        elif self.year < d2.year:
            return False
        else:
            if self.month > d2.month:
                return True
            elif self.month < d2.month:
                return False
            else:
                if self.day > d2.day:
                    return True
                elif self.day < d2.day:
                    return False
                else:
                    return False
    
    def diff(self, d2):
        """
        Returns an integer representing the number of days
        between self and d2
        """
        self_copy = self.copy()
        count = 0
        if self_copy.isBefore(d2):
            while self_copy.isBefore(d2):
                self_copy.tomorrow()
                count -= 1
        elif self_copy.isAfter(d2):
            while self_copy.isAfter(d2):
                self_copy.yesterday()
                count += 1
        return count
                
d = Date(11, 9, 2011)
d2 = Date(1, 1, 1899)
print(d.diff(d2))
print(d)
print(d2)

        