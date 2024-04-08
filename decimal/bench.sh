for i in $(seq 0 100 1000)
do
    echo $i >> results.txt
    /usr/bin/time -f "%U" -o results.txt -a ./mandelbrot_float      1000 1000 $i > /dev/null
    /usr/bin/time -f "%U" -o results.txt -a ./mandelbrot_double     1000 1000 $i > /dev/null
    /usr/bin/time -f "%U" -o results.txt -a ./mandelbrot_decimal32  1000 1000 $i > /dev/null
    /usr/bin/time -f "%U" -o results.txt -a ./mandelbrot_decimal64  1000 1000 $i > /dev/null
    /usr/bin/time -f "%U" -o results.txt -a ./mandelbrot_decimal128 1000 1000 $i > /dev/null
done
