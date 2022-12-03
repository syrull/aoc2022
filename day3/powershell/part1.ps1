$Sum = 0
$Alphabet = @()
97..122 | Foreach-Object { $Alphabet += [char]$_ }
65..90 | Foreach-Object { $Alphabet += [char]$_ }

(Get-Content "../input") | ForEach-Object {
    $FirstHalf = [char[]]$_.Substring(0, $_.Length / 2)
    $SecondHalf = [char[]]$_.Substring($_.Length / 2)
    $Common = @()
    $FirstHalf | ForEach-Object {
        if ($SecondHalf -cmatch $_) {
            $Common += $_
        }
    }
    $Common | Select-Object -Unique | ForEach-Object {
        For ($i = 0; $i -lt $Alphabet.Length; $i++) {
            if ($_ -cmatch $Alphabet[$i]) {
                $Sum += $i + 1
            }
        }
    }
}

$Sum