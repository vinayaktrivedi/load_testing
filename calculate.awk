BEGIN{
$count=0;
$sum=0;
}
{
print $1;
$count=$count+1;
$sum=$sum+$1;
}
END{
print $sum"\n"$count;
}
