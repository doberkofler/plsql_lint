create or replace
function square(p in number) return number
is
begin
	-- return the square of "p"
	return p * p;
end;
/
