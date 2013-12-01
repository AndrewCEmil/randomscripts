set term png
set output "monthly.png"

set xdata time
set timefmt "%Y-%m"
set format x "%Y-%m"
plot "monthly.data" using 1:2 t "total" with lines, "monthly.data" using 1:3 t "unique" with lines
set xrange ["2009-01":"2014-03"]
