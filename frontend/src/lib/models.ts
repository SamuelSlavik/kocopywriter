export type User = {
  id: string;
  email: string;
}
export type Credentials = {
  email: string;
  password: string;
}
export type Token = {
  access_token: string;
  token_type: string;
}


// HEADLINE ----------------------------------------------------------------------
export type Headline = {
  text: string;
}

// REFERENCES ----------------------------------------------------------------------
export type Reference = {
  id: string
  order: number
  name: string
  position: string
  url: string
  description: string
  image: string
}
export type NewReference = {
  order: number
  name: string
  position: string
  url: string
  description: string
  image: any
}

// POSTS ----------------------------------------------------------------------
export type Post = {
  id: string
  title: string
  image?: string
  short: string
  content: string
  date: string
}
export type NewPost = {
  title: string
  image?: string
  short: string
  content: string
  date: string
}

// IMAGES ----------------------------------------------------------------------
export type Image = {
  id: string
  url: string
  name: string
}
export type NewImage = {
  image: any
  name: string
}

// PRICE LIST ITEM ----------------------------------------------------------------------
export type PriceListItem = {
  id: string
  title: string
  description?: string
  second_description?: string
  items: ItemWithPrice[]
}
export type NewPriceListItem = {
  title?: string
  description?: string
  second_description?: string
  items: ItemWithPrice[]
}
export type ItemWithPrice = {
  name: string
  price: number
}

// BRANDS ----------------------------------------------------------------------
export type Brand = {
  id: string
  name: string
  image: any
}
export type NewBrand = {
  name: string
  image: any
}

// Projects -----------------------------------------------------------------------
export type Project = {
  id: string
  order: number
  name: string
  task: string
  description: string
  images: any[]
}
export type NewProject = {
  order: number
  name: string
  task: string
  description: string
  images: any[]
}