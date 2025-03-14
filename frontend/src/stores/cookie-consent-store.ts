import {defineStore} from "pinia";

export const useCookieConsentStore: any = defineStore(
    'cookieConsent', {
        state: (): any => ({
            set: false,
            technical: false,
            analytical: false,
        }),
        actions: {
            setCookieConsent (enabled: Boolean): void {
                this.set = true;
                this.technical = enabled;
                this.analytical = enabled;

                if (enabled) {
                    localStorage.setItem(
                        "cookieConsentAnalytical", this.analytical,
                    );
                    localStorage.setItem(
                        "cookieConsentTechnical", this.technical,
                    );
                } else {
                    localStorage.removeItem("cookieConsent");
                }
            },

            setAnalytical (enabled: Boolean): void {
                this.set = true
                this.analytical = enabled;

                this.updateLocalStorage();
            },

            setTechnical (enabled: Boolean): void {
                console.log("setTechnical", enabled);
                this.set=true
                this.technical = enabled;

                this.updateLocalStorage();
            },

            updateLocalStorage(): void {
                console.log('hello')
                if (this.analytical) {
                    localStorage.setItem("cookieConsentAnalytical", this.analytical);
                } else {
                    localStorage.removeItem("cookieConsentAnalytical");
                }

                if (this.technical) {
                    localStorage.setItem("cookieConsentTechnical", this.technical);
                } else {
                    localStorage.removeItem("cookieConsentTechnical");
                }
            },

            setSet (enabled: Boolean): void {
                this.set = enabled;
            },

            setTechnicalOnly (enabled: Boolean): void {
                this.technical = enabled;
            },

            setAnalyticalOnly (enabled: Boolean): void {
                console.log("setAnalyticalOnly", enabled);
                this.analytical = enabled;
            }
        }
    }
)