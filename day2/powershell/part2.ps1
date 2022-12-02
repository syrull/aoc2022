$PlayerScore = 0

(Get-Content -Path "../input") | ForEach-Object {
    if ($_[2] -eq "X") {
        if ($_[0] -eq "C") {
            $PlayerScore += 2
        } elseif ($_[0] -eq "A") {
            $PlayerScore += 3
        } else {
            $PlayerScore += 1
        }
    } elseif ($_[2] -eq "Y") {
        if ($_[0] -eq "A") { 
            $PlayerScore += 4
        } elseif ($_[0] -eq "B") {
            $PlayerScore += 5
        } else {
            $PlayerScore += 6
        }
    } elseif ($_[2] -eq "Z") {
        if ($_[0] -eq "B") {
            $PlayerScore += 9
        } elseif ($_[0] -eq "C") {
            $PlayerScore += 7
        } else {
            $PlayerScore += 8
        }
    }
}

$PlayerScore
