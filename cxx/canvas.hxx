#ifndef CANVAS_HXX
#define CANVAS_HXX

#include <iostream>
#include <string>
#include <vector>

#include "rgba.hxx"

namespace img
{
  class canvas
  {
  public:
    bool create(unsigned width  = WIDTH_DEF,
                unsigned height = HEIGHT_DEF);
    bool create(unsigned width,
                unsigned height,
                std::vector<rgba>&& pixels);

    void fill(const img::rgba& value);
    bool reflect_hor();
    bool reflect_ver();

    void clear() noexcept;
    bool empty() const noexcept;
    unsigned width()  const noexcept;
    unsigned height() const noexcept;
    const img::rgba* data() const noexcept;

  private:
    static constexpr unsigned WIDTH_MIN  =    1;
    static constexpr unsigned HEIGHT_MIN =    1;
    
    static constexpr unsigned WIDTH_DEF  =  512;
    static constexpr unsigned HEIGHT_DEF =  512;

    static constexpr unsigned WIDTH_MAX  = 2048;
    static constexpr unsigned HEIGHT_MAX = 2048;
       
    bool correct(unsigned int width, unsigned int height) const noexcept;

    unsigned _width  = 0;
    unsigned _height = 0;

    std::vector<img::rgba> _pixels;

    #if defined(IMAGE)
    friend
    std::ostream& operator<<(std::ostream& out, const img::canvas& in);
    #endif
  };

  img::canvas make_checker(bool mark = false);

  template<typename T>
  img::canvas read(const std::string& fname);
}

#endif // CANVAS_HXX
