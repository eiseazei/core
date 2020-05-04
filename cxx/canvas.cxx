#include "canvas.hxx"

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

#include "colors.hxx"
#include "rgba.hxx"

bool img::canvas::create(unsigned width, unsigned height)
{
  bool good = correct(width, height);

  if(good)
  {
    _width  = width;
    _height = height;

    _pixels.resize(_width * _height);
  }

  return good;
}

bool img::canvas::create(unsigned width,
                         unsigned height,
                         std::vector<img::rgba>&& pixels)
{
  bool test1 = correct(width, height);
  bool test2 = ((width * height) == pixels.size());
  bool good = test1 && test2;

  if(good)
  {
    _width  = width;
    _height = height;

    _pixels = std::move(pixels); // move assign
  }

  return good;
}

void img::canvas::fill(const img::rgba& value)
{
  _pixels.assign(_width * _height, value);
}

bool img::canvas::reflect_hor()
{
//    0  1  2  3  4
//    5  6  7  8  9
//   10 11 12 13 14
// 
//   10 11 12 13 14
//    0  1  2  3  4
//    5  6  7  8  9

  bool good = !empty();
  
  if(good)
  {
    auto first1 = _pixels.begin();
    auto first2 = _pixels.end() - _width;
    
    while(first1 < first2)
    {
      std::swap_ranges(first1, first1 + _width, first2);
      
      first1 += _width;
      first2 -= _width;
    }
  }

  return good;
}

bool img::canvas::reflect_ver()
{
  //  0  1  2  3  4
  //  5  6  7  8  9
  // 10 11 12 13 14

  //  4  3  2  1  0
  //  9  8  7  6  5
  // 14 13 12 11 10

  bool good = !empty();

  if(good)
  {
    unsigned beg = 0;
    unsigned end = 0;

    for(unsigned row = 0; row < _height; ++row)
    {
      beg = row * _width;
      end = beg + _width - 1u;

      while(beg < end)
      {
        std::swap(_pixels[beg], _pixels[end]);

        beg += 1;
        end -= 1;
      }
    }
  }

  return good;
}

void img::canvas::clear() noexcept
{
  _width  = 0;
  _height = 0;

  _pixels.clear();
}

bool img::canvas::empty() const noexcept
{
  return _pixels.empty();
}

unsigned img::canvas::width() const noexcept
{
  return _width;
}

unsigned img::canvas::height() const noexcept
{
  return _height;
}

const img::rgba* img::canvas::data() const noexcept
{
  return _pixels.data();
}

bool img::canvas::correct(unsigned width, unsigned height) const noexcept
{
  return (width  >=  WIDTH_MIN && width  <=  WIDTH_MAX) &&
         (height >= HEIGHT_MIN && height <= HEIGHT_MAX);
}

#if defined(IMAGE)
namespace img
{
  std::ostream& operator<<(std::ostream& out, const img::canvas& in)
  {
//     for(const auto& p : in._pixels)
//     {
//       out << p;
//     }
    
    for(auto itr = in._pixels.begin(); itr != in._pixels.end(); ++itr)
    {
      out << std::distance(in._pixels.begin(), itr);
      out << " ";
      out << *itr;
    }

    return out;
  }
}
#endif

img::canvas img::make_checker(bool mark)
{
  const auto teal = img::make_rgba(img::colors::teal);
  const auto gray = img::make_rgba(img::colors::gray);
  auto temp = gray;

  if(mark)
  {
    temp = img::make_rgba(img::colors::navy);
  }

  constexpr unsigned width  = 256;
  constexpr unsigned height = 256;

  std::vector<img::rgba> pixels(width * height);

  for(unsigned row = 0; row < height; ++row)
  {
    for(unsigned col = 0; col < width; ++col)
    {
      unsigned positon = width * row + col;

      if((row < 4) && (col < 4))
      {
        pixels[positon] = temp;
      }
      else if((row & 4) == (col & 4))
      {
        pixels[positon] = teal;
      }
      else
      {
        pixels[positon] = gray;
      }
    }
  }

  img::canvas canvas;
  
  canvas.create(width, height, std::move(pixels));

  return canvas;
}

template <typename T>
img::canvas img::read(const std::string& fname)
{
  T image;
  
  return image.read(fname);
}
