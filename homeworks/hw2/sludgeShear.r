library(tidyverse)
sludge <- data.frame(
    Sludge_Type = c(
        "S1",
        "S1",
        "S1",
        "S1",
        "S1",
        "S1",
        "S2",
        "S2",
        "S2",
        "S2",
        "S2",
        "S2",
        "S3",
        "S3",
        "S3",
        "S3",
        "S3",
        "S3"
    ),
    Shear_Stress = c(
        3.8,
        5.4,
        9,
        14.1,
        23.1,
        35.7,
        1.7,
        3.6,
        7.5,
        15,
        36.9,
        74.2,
        15.4,
        17.3,
        21.3,
        28.7,
        50.6,
        87.9
    ),
    Shear_Rate = c(
        1.8,
        3.7,
        7.3,
        14.7,
        36.7,
        73.4,
        1.8,
        3.7,
        7.3,
        14.7,
        36.7,
        73.4,
        1.8,
        3.7,
        7.3,
        14.7,
        36.7,
        73.4
    )
)

S1_model <-
    lm((log(y) ~ log(x)),
       data = sludge %>% filter(Sludge_Type == "S1") %>% mutate(x = Shear_Rate, y = Shear_Stress)
    )
S2_model <-
    lm(y ~ x,
       data = sludge %>% filter(Sludge_Type == "S2") %>% mutate(x = Shear_Rate, y = Shear_Stress))
S3_model <-
    lm(y ~ x,
       data = sludge %>% filter(Sludge_Type == "S3") %>% mutate(x = Shear_Rate, y = Shear_Stress))


ggplot(sludge,
       aes(
           x = Shear_Rate,
           y = Shear_Stress,
           shape = Sludge_Type,
           color = Sludge_Type
       )) +
    geom_point(size = 3) +
    labs(
        x = "Shear Rate (1/s)",
        y = "Shear Stress (N/m²)",
        shape = "Sludge Type",
        color = "Sludge Type"
    ) +
    theme_classic() +
    geom_smooth(
        size = 0.5,
        method = "nls",
        formula = "y~a*x^b",
        method.args = list(start = c(a = 1, b = 1)),
        se = FALSE,
        data = subset(sludge, Sludge_Type == "S1")
    ) +
    geom_smooth(
        size = 0.5,
        method = "lm",
        formula = 'y ~ x',
        se = FALSE,
        data = subset(sludge, Sludge_Type == "S2")
    ) +
    geom_smooth(
        size = 0.5,
        method = "lm",
        formula = 'y ~ x',
        se = FALSE,
        data = subset(sludge, Sludge_Type == "S3")
    ) + theme(
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.background = element_blank(),
        panel.background = element_rect(fill = "transparent", colour = NA),
        plot.background = element_rect(fill = "transparent", colour = NA)
    )