select a.row_num, b.col_num, sum(a.value*b.value)
from a, b
where a.col_num = b.row_num
group by a.row_num, b.col_num;
/*2|3|2874*/
