<script setup lang="ts">

</script>

<template>
  <div class="about-background" id="section-about">
    <Container class="section-about">
      <div class="section-about__content">
        <div>
          <h2>
            Účelnou jinakostí řeším problémy už odmala
          </h2>
          <br/>
          <p>
            Kvůli vadě řeči jsem zvyklý hledat alternativní cesty tam, kde ty standardní nefungují. A díky kreativitě a drzosti je vždycky najdu.
          </p>
          <br/>
          <p>
            <b><span class="accent">✶</span> Když mi na vejšce učitel odmítl udělit zápočet, dokud mu nezodpovím všechny otázky bez jediného zadrhnutí…</b>
          </p>
          <br/>
          <p>
            …sehnal jsem kontakt na jeho platonickou lásku – známou herečku – domluvil se s ní a při dalším zkoušení mu ji dal k telefonu.
            Aby poznal, jaké to je, když toho máte hodně na srdci, ale nemůžete se vymáčknout.
            A hned po nervózním doblekotání v sobě jako zázrakem objevil kousek empatie.
          </p>
          <br/>
          <p>
            <b>
              <span class="accent">✶</span> Když jsem při náboru k policii měl tetování, která by v uniformě byla vidět…
            </b>
          </p>
          <br/>
          <p>
            …zakryl jsem je make-upem a schválně si vzal triko s krátkým rukávem, aby byla vidět všechna místa, kde tetování mám.
            Náborářky si jich celý den nevšimly. Tím jsem jim ukázal, že kérky mě nijak
            nediskvalifikují – i když předpisy zakazují „mít v uniformě viditelná tetování“.
          </p>
          <br/>
          <p>
            <b>
              Problém <span class="accent">→</span> netradiční řešení <span class="accent">→</span> výsledek
            </b>
          </p>
          <br/>
          <p>
            Tuhle rovnici uplatňuju pořád.
          </p>
          <br/>
          <p>
            Za posledních <b>9 let</b> jsem tomu dal těch pověstných <b>10 000 hodin</b>.
            A z talentu vybrousil byznysově použitelný skill, který obohatil už více než <b>150 klientů</b>.
            Nyní má cenovku <b>1 818 Kč/hod</b>.
          </p>
        </div>
      </div>
    </Container>
    <div class="about-wallpaper">
      <img src="../../assets/images/wallpapers/w-dark-2.jpg" alt="Logo" />
    </div>
  </div>
</template>

<style>
.about-background {
  position: relative;
  width: 100%;
  height: 100%;
}

.about-wallpaper {
  img {
    width: 800px;
    left: -400px;
    height: auto;
    position: absolute;
    z-index: -1;
    top: 50%;
    transform: translateY(-50%);
    @media (max-width: 1024px) {
      position: relative;
      width: 100%;
      left: auto;
      top: auto;
      transform: none;
    }
  }
}

.section-about {
  @media (max-width: 1024px) {
    display: flex;
    flex-direction: column;
    margin: 3rem 0;
  }

  .section-about__content {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    gap: 2rem;
    width: 70%;
    margin-left: 25%;
    text-align: left;
    justify-content: center;
    @media (max-width: 1024px) {
      width: 100%;
      min-height: auto;
      margin-left: auto;
    }

    b {
      color: var(--primary);
    }
  }
}
</style>