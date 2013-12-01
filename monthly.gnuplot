set term png
set output "monthly.png"
set size 1,1
set terminal png enhanced size 1024,768 font 'Veranda,12'

set xdata time
set timefmt "%Y-%m"
set format x "%Y-%m"
plot "monthly.data" using 1:2 t "total" with lines, "monthly.data" using 1:3 t "unique" with lines
