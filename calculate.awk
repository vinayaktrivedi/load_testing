BEGIN{
c=0;
s=0;
}
{ 
c+=1;
s+=$1;
}
END{
average=s/(2000*c);
print average;
}
