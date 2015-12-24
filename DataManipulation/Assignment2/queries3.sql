select a.docid, b.docid, sum(a.count * b.count)
from Frequency a , Frequency b
on a.term = b.term
where a.docid = '10080_txt_crude' and b.docid = '17035_txt_earn'
group by a.docid, a.docid;
/*19*/

CREATE VIEW v AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select A.docid, B.docid, sum(A.count * B.count) as similarity
from v A, v B
on A.term = B.term
where A.docid = 'q' and B.docid != 'q'
group by A.docid, B.docid
order by similarity desc limit 10;
/*6*/
