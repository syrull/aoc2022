$Sum = 0
$Alphabet = @()
97..122 | Foreach-Object { $Alphabet += [char]$_ }
65..90 | Foreach-Object { $Alphabet += [char]$_ }

$Input_ = Get-Content "../input"
$Chunked = for ($i = 0; $i -lt $Input_.Length; $i += 3) { ,($Input_ | Select-Object -Skip $i -First 3) }

foreach ($chunk in $Chunked) {
    [char[]]$chunk[0] | ForEach-Object {
        $a = ([string]$chunk[1].contains($_))
        $b = ([string]$chunk[2].contains($_))
        if (($a -eq $true) -and ($b -eq $true)) {
            For ($i = 0; $i -lt $Alphabet.Length; $i++) {
                if ($_ -cmatch $Alphabet[$i]) {
                    $Sum += $i + 1
                }
            }
            continue
        }
    }
}
$Sum