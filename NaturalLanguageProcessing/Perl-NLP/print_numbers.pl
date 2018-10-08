#!/usr/bin/perl
use warnings;
use strict;

print "Enter a positive integer: ";
my $iteration_count = <>; # represents the number of times a loop must run
for (my $i=1;$i <= $iteration_count; $i++) {
	for(my $j=1;$j <= $i; $j++){
		print "$j ";
	}
	print "\n";
}
