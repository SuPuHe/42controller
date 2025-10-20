input.onGesture(Gesture.LogoUp, function () {
	
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendValue("sigleft", 1)
    basic.showIcon(IconNames.SmallHeart)
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendValue("sigright", 1)
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.LogoDown, function () {
    radio.sendValue("sigdown", 1)
    basic.showIcon(IconNames.TShirt)
})
radio.setGroup(228)
basic.forever(function () {
	
})
