for fastaFile in $(ls $1*.fasta);
do 
#echo ${fastaFile%.fasta}.msa;
muscle -in $fastaFile -out ${fastaFile%.fasta}.msa -quiet;
done;
