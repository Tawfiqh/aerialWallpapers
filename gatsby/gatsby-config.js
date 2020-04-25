/**
 * Configure your Gatsby site with this file.
 *
 * See: https://www.gatsbyjs.org/docs/gatsby-config/
 */
const path = require(`path`)

module.exports = {
    siteMetadata: {
      title: 'Aerial '
    },
  plugins: [
      {
        resolve: `gatsby-source-filesystem`,
        options: {
          name: `images`,
          path: path.join(__dirname, `static`, `thumbnails`),
        },
      },
      `gatsby-plugin-sharp`,
      `gatsby-transformer-sharp`
  ]
}
