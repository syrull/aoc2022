$sum = 0
$sums = @()
(Get-Content -Path "../input") | ForEach-Object {
    $i = [int]$_ 
    if ($i -eq 0) {
        $sums += $sum
        $sum = 0
    }
    $sum += $i
}
$sum = 0
($sums | Sort-Object)[-1..-3] | ForEach-Object { $sum += $_ }
$sum