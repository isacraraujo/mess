var body: some View {
    ZStack {
        background
        toggleButtonBackground
        colorCircle
            .mask(capsuleMask)
        colorCircle
            .mask(circleMask)
            .ontapGesture { toggle()}
    }
    .onAppear { animateColor.toggle() }
}