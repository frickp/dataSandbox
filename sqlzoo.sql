# https://sqlzoo.net/wiki/Helpdesk_Easy_Questions

/* number 1 - works! */
select
  Call_date,  Call_ref
from 
  helpdesk.Issue
where
  detail like '%index%'
  and 
  detail like '%oracle%';
  
/* number 2 - works!  */
select 
  i.call_date, sub.first_name, sub.last_name
from
  helpdesk.Issue i
join
    (select
      *
    from 
      helpdesk.Caller
    where
      first_name = 'Samantha'
      and
      last_name = 'Hall') sub
on
  i.Caller_id = sub.Caller_id
where
  i.call_date like '%2017-08-14%';

/* number 3 - works! */
select
  Status as status, count(*) as Volume
from
  helpdesk.Issue
group by
  Status

/* number 4 - works!*/
select
  count(*) as mlcc
from
  Level l
join
    (select
      s.Level_code
    from
      Issue i
    join
      Staff s
    on
      i.Assigned_to = s.Staff_code) sub
on
  l.Level_code = sub.Level_code
where
  l.Manager = 'Y';

/* number 5 - works! */
select
  sh.Shift_date Shift_date, sh.Shift_type Shift_type, st.First_name first_name, st.last_name last_name
from
  Shift sh
inner join
  Staff st
on
  sh.Manager = st.Staff_code
order by
  sh.Shift_date, sh.Shift_type;

/* Now, try the medium level questions */

/* number 6: works!
List the Company name and the number of calls for those companies with more than 18 calls.
*/
select
  cu.Company_name Company_name, sub.num_calls num_calls
from
  Customer cu
join
    (select
      c.Company_ref as Company_ref, count(*) as num_calls
    from
      Caller c
    join
      Issue i
    on
      c.Caller_id = i.Caller_id
    group by
      c.Company_ref) sub
on
  cu.Company_ref = sub.Company_ref
where
  num_calls > 18
order by
  Company_name desc;

/* number 7: works!
Find the callers who have never made a call. Show first name and last name
*/

select
  c.First_name, c.Last_name
from
  Caller c
left join
  Issue i
on
  c.Caller_id = i.Caller_id
where
  i.Caller_id is null;
 
/* number 8: CLOSE ENOUGH! This one is annoying, can't get names
For each customer show: Company name, contact name, 
number of calls where the number of calls is fewer than 5
*/

select
  *
from
  Customer cu
join
    (select
      c.Company_ref Company_ref, count(*) num_calls
    from
      Issue i
    join
      Caller c
    on
      i.Caller_id = c.Caller_id
    group by
      c.Company_ref
    having
      count(*) < 5) sub
on
  cu.Company_ref = sub.Company_ref

/* Number 9: in progress
For each shift show the number of staff assigned. Beware that some roles may be NULL
and that the same person might have been assigned to multiple roles
(The roles are 'Manager', 'Operator', 'Engineer1', 'Engineer2').
*/

select
  sub.Shift_date, sub.Shift_type, sum(emp) counts
from 
    (select
      Shift_date, Shift_type, Manager emp
    from
      Shift
    union all 
    select
      Shift_date, Shift_type, Operator emp
    from
      Shift
    union all 
    select
      Shift_date, Shift_type, Engineer1 emp
    from
      Shift
    union all 
    select
      Shift_date, Shift_type, Engineer2 emp
    from
      Shift) sub
group by sub.Shift_date, sub.Shift_type;

case when Engineer2 is null then 0 else 1 end as emp
  
case when distinct emp

/*  
SELECT player_name,
       year,
       CASE WHEN year = 'SR' THEN 'yes'
            ELSE NULL END AS is_a_senior
  FROM benn.college_football_players  

select vend, year, 1 month, [I1_DOLS] Dols, [I1_QTY] Qty
from yourtable
union all
select vend, year, 2 month, [I2_DOLS] Dols, [I2_QTY] Qty
from yourtable
union all
select vend, year, 3 month, [I3_DOLS] Dols, [I3_QTY] Qty
from yourtable

*/
Caller_id	Company_ref	First_name	Last_name
85	145	Samantha	Hall
