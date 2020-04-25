import React from "react"
import { useStaticQuery, graphql } from "gatsby" // to query for image data
import JSONData from "../../content/output_parsed_file_list.json"
import Img from "gatsby-image"


const JSONbuildtime = () => {


    const imgdata = useStaticQuery(graphql`
        query {
          allFile{
            edges {
              node {
                base
                childImageSharp {
                  fluid(maxWidth: 1000) {
                      ...GatsbyImageSharpFluid
                  }
                }
              }
            }
          }
        }
    `)

    function assetButtonLink(data, key, title){
        if(data[key]){
            return (
              <>
                <a href={data[key]}>
                    <span role="img" aria-label="cinema">🎬</span> Watch {title}
                </a>
                <br  />
              </>
            )
        }
    }

    function getImageFromGraphForId(imageId, title, extension="jpeg"){
        {/* <Img fixed={data.file.childImageSharp.fixed} /> */}
        {/* <img src={"thumbnails/" +data.id +".jpeg"} alt={data.accessibilityLabel} title={data.accessibilityLabel} /> */}

        var imageData = imgdata.allFile.edges.find(edge =>edge.node.base === imageId);

        return(<div className="image_wrapper">
                  <Img fluid={imageData.node.childImageSharp.fluid} alt={title} />
               </div>)
    }


return(
  <div>

      <h1>Aerial wallpapers </h1>
      <p>Amazing footage from AppleTV default wallpapers. Mostly drone footage of various cities. Features some satellite footage and underwater footage too! Built from https://github.com/Tawfiqh/aerialWallpapers</p>

      <div className="asset_container" >


          {JSONData.map((data, index) => {

            return (
            <div className="asset"  key={`asset_${index}`}>
                <h2>{data.accessibilityLabel} <em>({data.id})</em></h2>

                {getImageFromGraphForId(data.id + ".jpeg", data.accessibilityLabel)}


                <div className="button_container" >
                    <p>
                    {assetButtonLink(data, "url", "")}
                    {assetButtonLink(data, "url-1080-SDR", "1080p")}
                    {assetButtonLink(data, "url-4K-SDR", <em>4K</em>)}
                    {assetButtonLink(data, "url-1080-H264", "1080p-H264")}
                    </p>


                    {(data["url-1080-HDR"] || data["url-4K-HDR"]) && <h4>HDR</h4>}
                    <p>
                    {assetButtonLink(data, "url-1080-HDR", "1080-HDR")}
                    {assetButtonLink(data, "url-4K-HDR", "4K-HDR ")}
                </p>
                </div>
            </div>
            )
          })}

      </div>



  </div>
)}
export default JSONbuildtime
