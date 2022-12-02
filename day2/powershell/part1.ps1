$PlayerScore = 0

(Get-Content -Path "../input") | ForEach-Object {
    if ($_[2] -eq "X") {
        if ($_[0] -eq "C") {
            $PlayerScore += 7
        } elseif ($_[0] -eq "A") {
            $PlayerScore += 4
        } else {
            $PlayerScore += 1
        }
    } elseif ($_[2] -eq "Y") {
        if ($_[0] -eq "A") { 
            $PlayerScore += 8
        } elseif ($_[0] -eq "B") {
            $PlayerScore += 5
        } else {
            $PlayerScore += 2
        }
    } elseif ($_[2] -eq "Z") {
        if ($_[0] -eq "B") {
            $PlayerScore += 9
        } elseif ($_[0] -eq "C") {
            $PlayerScore += 6
        } else {
            $PlayerScore += 3
        }
    }
}

$PlayerScore
