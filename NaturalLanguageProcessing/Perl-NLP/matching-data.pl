#!/usr/bin/perl
#Program: matching-data.pl

sub testre {
	my $re=shift;
	my $line = shift;
	if($line =~ /$re/){
		print "/$re/ MATCH: $`>>>$&<<<$'";
	} else{
		print "/$re/ NOMATCH: $line";
	}
}

while (<DATA>) {
	&testre('book',$_);# testing /book/
}

__DATA__
This line has book in it
How about textbook?
This is capitalized word "Book"
