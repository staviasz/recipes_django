from unittest import TestCase
from utils.make_pagination import make_pagination_range, make_pagination
from recipes.models import Recipe
from django.http import HttpRequest

class PaginationTest(TestCase):
  def test_make_pagination_range_returns_a_pagination_range(self):
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=1
    )['pagination']
    self.assertEqual([1,2,3,4], pagination)

  def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
    #current page = 2 - qty page = 2 middle page = 2
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=2
    )['pagination']
    self.assertEqual([1,2,3,4], pagination)

    #current page = 3 - qty page = 2 middle page = 2
    #HERE RANGE SHOULD CHANGE
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=3
    )['pagination']
    self.assertEqual([2,3,4,5], pagination)

  def test_make_sure_middle_ranges_are_correct(self):
    #current page = 4 - qty page = 2 middle page = 2
    #HERE RANGE SHOULD CHANGE
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=4
    )['pagination']
    self.assertEqual([3,4,5,6], pagination)

    #current page = 10 - qty page = 2 middle page = 2
    #HERE RANGE SHOULD CHANGE
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=10
    )['pagination']
    self.assertEqual([9,10,11,12], pagination)

  def test_make_pagination_range_static_stop_range(self):
    #current page = 18 - qty page = 2 middle page = 2
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=18
    )['pagination']
    self.assertEqual([17,18,19,20], pagination)

    #current page = 19 - qty page = 2 middle page = 2
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=19
    )['pagination']
    self.assertEqual([17,18,19,20], pagination)

    #current page = 20 - qty page = 2 middle page = 2
    pagination = make_pagination_range(
      page_range=list(range(1, 21)),
      qty_pages=4,
      current_page=20
    )['pagination']
    self.assertEqual([17,18,19,20], pagination)

  def test_make_pagination_except_value_error(self):
    request = HttpRequest()
    request.GET = {'page':'invalid value'}
    queryset = [1,2,3,4,5]

    page_obj, pagination_range = make_pagination(request, queryset, 3)

    self.assertEqual(page_obj.number, 1)
    self.assertIsInstance (pagination_range, dict)
