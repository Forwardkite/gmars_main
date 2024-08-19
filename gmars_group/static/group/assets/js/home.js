//GSAP HORIZONTAL SCROLLER
    let scroll_tl = gsap.timeline({
        scrollTrigger: {
            trigger: '.division_3',
            start: "top center",
            scrub: true,
            end: "+=300",
        }
    }),
    facts = [...document.querySelectorAll('.card')]
    scroll_tl.to('.division_3 .big', {
        scale: 1.5,
        duration: 1,
        ease: "slow"
    })
    scroll_tl.to(facts, {
        xPercent: -85 * (facts.length - 1),
        scrollTrigger: {
            trigger: ".cards",
            start: "center center",
            pin: true,
            scrub: 1,
            snap: 0 / (facts.length - 1),
            end: () => `+=4320`
        }
    });
