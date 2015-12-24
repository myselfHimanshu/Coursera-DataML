select count(*) from frequency where docid="10398_txt_earn";
/*138*/

select count(term) from frequency where docid="10398_txt_earn" and count=1;
/*110*/

select count(term) from frequency
where docid in ("10398_txt_earn","925_txt_trade") and count=1;
/*335*/

select count(distinct docid) from frequency
where term="law" or term="legal";
/*58*/

select count(*) from
( select count(count) s from frequency
  group by docid
  having s>300);
/*11*/

select count(*) from(
select distinct docid from frequency
where term = ( 'world' )
intersect
select distinct docid from frequency
where term =( 'transactions' ));
/*3*/
