import React, { useState } from "react";
import Sidebar from "../Sidebar";
import Navbar from "../Navbar";
import Layout from "../Layout";
import DataTable from "react-data-table-component";
import './Dashboard.css'

export default function Dashboard() {
  const data = [{ name: "dsfksdfs", last_runtime: 32423 }, { name: "fnsj" }];
  const column = [
    {
      name: (
        <p style={{ fontSize: "16px", fontWeight: "700", color: "#1c2b3e" }}>
          Query Name
        </p>
      ),
      selector: (row) => row.name,
      sortable: true,
      width: "25%",
    },
    {
      name: (
        <p style={{ fontSize: "16px", fontWeight: "700", color: "#1c2b3e" }}>
          Last Search
        </p>
      ),
      selector: (row) =>
        row.last_runtime === null ? "Not Yet Executed" : "fsdjgn",
      sortable: true,
      width: "30%",
    },
  ];
  return (
    <Layout>
      <div className="main_total">
        <div>DASHBOARD</div>
        <DataTable
          style={{ paddingTop: "-20px" }}
          columns={column}
          data={data}
          pagination
          fixedHeader
          noHeader={true}
          subHeader
          //   subHeaderComponent={
          //     <input
          //       type="search"
          //       placeholder="Search here"
          //       className="w-25 form-control"
          //       value={search}
          //       onChange={(e) => {
          //         setSearch(e.target.value);
          //       }}
          //     />
          //   }
        />
      </div>
    </Layout>
  );
}
